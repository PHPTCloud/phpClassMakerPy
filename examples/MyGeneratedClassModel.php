<?php
/**
 * @class MyGeneratedClassModel
 * @package AppNamespace 
 */

namespace AppNamespace;

class MyGeneratedClassModel extends AbstractClassModel implements ByTheWay, UseImplements, ThroughCommaSign
{
	/**
	 * @var string
	 */
	private $somePrivateField; 

	/**
	 * @var WithCustomType
	 */
	protected $someProtectedField; 

	/**
	 * @var WithGettersAndSetters
	 */
	public $publicField; 

	/**
	 * @var string
	 */
	public $otherField; 

	/**
	 * @var bool
	 */
	public $isAwesomePyScript; 

	/**
	 * @return string
	 */
	public function getSomePrivateField(): ?string
	{
		return $this->somePrivateField;
	}

	/**
	 * @param string $somePrivateField
	 * @return this
	 */
	public function setSomePrivateField(string $somePrivateField): self
	{
		$this->somePrivateField = $somePrivateField;
		return $this;
	}

	/**
	 * @return WithCustomType
	 */
	public function getSomeProtectedField(): ?WithCustomType
	{
		return $this->someProtectedField;
	}

	/**
	 * @param WithCustomType $someProtectedField
	 * @return this
	 */
	public function setSomeProtectedField(WithCustomType $someProtectedField): self
	{
		$this->someProtectedField = $someProtectedField;
		return $this;
	}

	/**
	 * @return WithGettersAndSetters
	 */
	public function getPublicField(): ?WithGettersAndSetters
	{
		return $this->publicField;
	}

	/**
	 * @param WithGettersAndSetters $publicField
	 * @return this
	 */
	public function setPublicField(WithGettersAndSetters $publicField): self
	{
		$this->publicField = $publicField;
		return $this;
	}

	/**
	 * @return string
	 */
	public function getOtherField(): ?string
	{
		return $this->otherField;
	}

	/**
	 * @param string $otherField
	 * @return this
	 */
	public function setOtherField(string $otherField): self
	{
		$this->otherField = $otherField;
		return $this;
	}

	/**
	 * @return bool
	 */
	public function getIsAwesomePyScript(): ?bool
	{
		return $this->isAwesomePyScript;
	}

	/**
	 * @param bool $isAwesomePyScript
	 * @return this
	 */
	public function setIsAwesomePyScript(bool $isAwesomePyScript): self
	{
		$this->isAwesomePyScript = $isAwesomePyScript;
		return $this;
	}

}